#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
交通事故赔偿金额预测计算器 —— 本地 Flask 后端
运行： pip install flask joblib numpy pandas scikit-learn
       python app.py
       浏览器打开 http://127.0.0.1:5000
"""
import os, json, joblib
import numpy as np
from flask import Flask, request, jsonify, render_template

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
app = Flask(__name__)

with open(os.path.join(BASE_DIR, 'model_meta.json'), 'r', encoding='utf-8') as f:
    META = json.load(f)

FEATURES_STAGE1 = META['features_stage1']
FEATURES_STAGE2 = META['features_stage2']
TARGET_COLS = META['target_cols']


def load_all_bundles(model_dir_name):
    model_dir = os.path.join(BASE_DIR, model_dir_name)
    bundles = {}
    for target in TARGET_COLS:
        safe_name = target.replace('/', '_').replace('(', '').replace(')', '')
        clf_path = os.path.join(model_dir, f'{safe_name}_\u5206\u7c7b\u5668.pkl')
        small_path = os.path.join(model_dir, f'{safe_name}_\u5c0f\u989d\u56de\u5f52.pkl')
        large_path = os.path.join(model_dir, f'{safe_name}_\u5927\u989d\u56de\u5f52.pkl')
        fallback_path = os.path.join(model_dir, f'{safe_name}_\u5146\u5e95\u4fe1\u606f.pkl')
        bundle = {
            'clf': joblib.load(clf_path) if os.path.exists(clf_path) else None,
            'reg_small': joblib.load(small_path) if os.path.exists(small_path) else None,
            'reg_large': joblib.load(large_path) if os.path.exists(large_path) else None,
        }
        if os.path.exists(fallback_path):
            fb = joblib.load(fallback_path)
            bundle['small_mean'] = fb.get('small_mean', np.nan)
            bundle['large_mean'] = fb.get('large_mean', np.nan)
        bundles[target] = bundle
    return bundles


BUNDLES_STAGE1 = load_all_bundles(META['model_dir_stage1'])
BUNDLES_STAGE2 = load_all_bundles(META['model_dir_stage2'])


def predict_one_target(bundle, x_row):
    if bundle['clf'] is None:
        return None, None
    label = int(bundle['clf'].predict(x_row)[0])
    if label == 1:
        pred = float(bundle['reg_large'].predict(x_row)[0]) if bundle['reg_large'] is not None else float(bundle.get('large_mean', np.nan))
    else:
        pred = float(bundle['reg_small'].predict(x_row)[0]) if bundle['reg_small'] is not None else float(bundle.get('small_mean', np.nan))
    return pred, ('\u5927\u989d\u8d54\u4ed8' if label == 1 else '\u5c0f\u989d\u8d54\u4ed8')


@app.route('/')
def index():
    return render_template(
        'index.html',
        feature_meta_stage1=META['feature_meta_stage1'],
        feature_meta_stage2=META['feature_meta_stage2'],
        features_stage1=FEATURES_STAGE1,
        features_stage2=FEATURES_STAGE2,
        target_cols=TARGET_COLS,
        metrics_summary=META['metrics_summary'],
    )


@app.route('/api/predict', methods=['POST'])
def api_predict():
    payload = request.get_json(force=True)
    stage = payload.get('stage', 'stage2')
    values = payload.get('values', {})

    if stage == 'stage1':
        feature_cols, bundles, meta = FEATURES_STAGE1, BUNDLES_STAGE1, META['feature_meta_stage1']
    else:
        feature_cols, bundles, meta = FEATURES_STAGE2, BUNDLES_STAGE2, META['feature_meta_stage2']

    row = []
    for c in feature_cols:
        v = values.get(c, meta[c]['\u9ed8\u8ba4\u503c(\u4e2d\u4f4d\u6570)'])
        try:
            v = float(v)
        except (TypeError, ValueError):
            v = meta[c]['\u9ed8\u8ba4\u503c(\u4e2d\u4f4d\u6570)']
        row.append(v)
    x = np.array(row, dtype=float).reshape(1, -1)

    results = {}
    for target in TARGET_COLS:
        pred, label = predict_one_target(bundles[target], x)
        results[target] = {'\u9884\u6d4b\u91d1\u989d': None if pred is None else round(pred, 2), '\u5224\u5b9a\u7c7b\u522b': label}

    return jsonify({'ok': True, 'stage': stage, 'results': results})


if __name__ == '__main__':
    import os
    port = int(os.environ.get('PORT', 5000))
    debug_mode = os.environ.get('FLASK_ENV') == 'development'
    app.run(debug=debug_mode, host='0.0.0.0', port=port)
