runner_config = {
    'iterations_per_run': 1500,
    'run_split': 0.6
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
    'dt': 0.05,
    'state': {
        'y': 0.,
        'dy': 0.,
        'ydot': 0.,
    },
    'params': {'m': 0.8},
    'speed_noise': 0.1,
    'altitude_noise': 0.01,
    'sy_min': -.5,
    'sy_max': .5
}
