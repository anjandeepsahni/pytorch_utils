from ._validate import _validate_param

__all__ = ['get_model_param_count', 'get_trainable_param_count']

def get_model_param_count(model):
    """
    Count total parameters in the PyTorch model.

    Parameters
    ----------
    model : nn.Module
        PyTorch model.

    Returns
    -------
    int
        Number of parameters in the model.
    """

    _validate_param(model, 'model', 'model')
    param_count = 0
    for p in model.parameters():
        val = p.size(0)
        if len(p.size()) > 1:
            val *= p.size(1)
        param_count += val
    return param_count


def get_trainable_param_count(model):
    """
    Count total trainable parameters in the PyTorch model.
    Parameters
    ----------
    model : nn.Module
        PyTorch model.
    Returns
    -------
    int
        Number of trainable parameters in the model.
    """

    _validate_param(model, 'model', 'model')
    param_count = 0
    for p in model.parameters():
        if p.requires_grad:
            val = p.size(0)
            if len(p.size()) > 1:
                val *= p.size(1)
            param_count += val
    return param_count
