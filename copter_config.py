logger_config = {
    'labels': ['dy', 'ydot', 'ydotdot', 'force_y', 'pred_dy'],
    'types':  ['float', 'float', 'float', 'float', 'float'],
    'keys':   {
        'state': ['dy', 'ydot', 'ydotdot'],
        'force': ['y'],
        'predicted_state': ['dy']
    }
}

predictor_config = {
    'serialization': {
        'path': '/tmp/pilot/default/copter',
        'save_freq': 1000
    }
}
