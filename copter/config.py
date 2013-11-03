runner_config = {
    'y_min': -500.,
    'y_max': 500.,
    'iterations_per_run': 2000,
    'target_threshold': .005
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

world_config = {
    'dt': 0.01,
    'state': {
        'y': 0.,
        'dy': 0.,
        'ydot': 0.,
    },
    'params': None,
    'noise': 0.1
}
