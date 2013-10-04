from collections import defaultdict

# define easy initializer for default dictionary


def d(obj, init):
    return defaultdict((lambda: obj), init)


config = d(None, {
    'logger': d(None, {
        # 'path': '/Users/simjega/Projects/HTM/Data/pendulum_logger.csv',
        'labels': ['xdot', 'theta', 'force_x', 'theta_pred_1'],
        'types': ['float', 'float', 'float', 'float'],
        'keys': d([], {'state': ['xdot', 'theta'],
                       'force': ['x'],
                       'predicted_state': ['theta']
                       })
    })
})
