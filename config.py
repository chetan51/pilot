from collections import defaultdict

# define easy initializer for default dictionary


def d(obj, init):
    return defaultdict((lambda: obj), init)


logger_config = d(None, {
    'labels': ['xdot', 'theta', 'force_x', 'theta_pred_1'],
    'types': ['float', 'float', 'float', 'float'],
    'keys': d([], {'state': ['xdot', 'theta'],
                   'force': ['x'],
                   'predicted_state': ['theta']
                   })
})
