from collections import defaultdict

# define easy initializer for default dictionary


def d(obj, init):
    return defaultdict((lambda: obj), init)


logger_config = d(None, {
    'labels': ['xdot', 'theta', 'force_x', 'pred_theta'],
    'types': ['float', 'float', 'float', 'float'],
    'keys': d([], {'state': ['xdot', 'theta'],
                   'force': ['x'],
                   'predicted_state': ['theta']
                   })
})

predictor_config = {
    'serialization': {	'path': '/Users/simjega/Projects/HTM/pilot/model/default',
                       'save_freq': 1000}
}
