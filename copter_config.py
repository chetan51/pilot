from collections import defaultdict

# define easy initializer for default dictionary


def d(obj, init):
    return defaultdict((lambda: obj), init)


logger_config = d(None, {
    'labels': ['dy', 'ydot', 'ydotdot', 'force_y', 'pred_dy'],
    'types': ['float', 'float', 'float', 'float', 'float'],
    'keys': d([], {'state': ['dy', 'ydot', 'ydotdot'],
                   'force': ['y'],
                   'predicted_state': ['dy']
                   })
})

predictor_config = {
    'serialization': {	'path': '/tmp/pilot/default/copter',
                       'save_freq': 1000}
}
