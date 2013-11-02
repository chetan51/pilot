runner_config = {
    'y_min': -500.,
    'y_max': 500.,
    'iterations_per_run': 2000
}

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
        'path': '/tmp/pilot/default/copter'
    }
}
