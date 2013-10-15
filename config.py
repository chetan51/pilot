from collections import defaultdict

# define easy initializer for default dictionary


def d(obj, init):
    return defaultdict((lambda: obj), init)


logger_config = d(None, {
    'labels': ['theta', 'thetadot', 'force_x', 'pred_theta'],
    'types': ['float', 'float', 'float', 'float'],
    'keys': d([], {'state': ['theta', 'thetadot'],
                   'force': ['x'],
                   'predicted_state': ['theta']
                   })
})

predictor_config = {
    'serialization': {	'path': '/tmp/pilot/default',
                       'save_freq': 1000}
}
