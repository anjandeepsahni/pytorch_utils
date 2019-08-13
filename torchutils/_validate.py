import torch.nn as _nn
import torch.optim as _optim


def _validate_param(val, name, paramType):
    supportedTypes = {
        'int': int,
        'str': str,
        'float': float,
        'model': _nn.Module,
        'optimizer': _optim.Optimizer,
        'scheduler': [_optim.lr_scheduler._LRScheduler,
                      _optim.lr_scheduler.ReduceLROnPlateau]
        }
    if paramType not in supportedTypes:
        raise TypeError(('INTERNAL ERROR: paramType must be one of {}, but got {}. '
                    'Please raise an issue on github.').format(supportedTypes, type(val)))
    curType = supportedTypes[paramType]
    if not isinstance(curType, list):
        curType = [curType]
    for ct in curType:
        if isinstance(val, ct):
            return
    typeStr = str(curType[0])
    raise TypeError('{} must be of type {}, but got {}.'.format(name, typeStr, type(val)))
