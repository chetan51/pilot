logger_config = {
    'labels': ['theta', 'thetadot', 'force_x', 'pred_theta'],
    'types':  ['float', 'float', 'float', 'float'],
    'keys':   {
        'state': ['theta', 'thetadot'],
        'force': ['x'],
        'predicted_state': ['theta']
    }
}

predictor_config = {
    'serialization': {
        'path': '/tmp/pilot/default/pendulum',
        'save_freq': 1000
    }
}
