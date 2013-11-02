logger_config = {
    'labels': ['dy', 'y', 'ydot', 'speed_y', 'pred_speed_y'],
    'types':  ['float', 'float', 'float', 'float', 'float'],
    'keys':   {
        'state': ['dy', 'y', 'ydot'],
        'action': ['speed_y']
    }
}

predictor_config = {
    'serialization': {
        'path': '/tmp/pilot/default/copter',
        'save_freq': 1000
    }
}
