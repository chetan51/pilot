import tempfile
import shutil

from nupic.frameworks.opf import [Model,CLAModel]

class Imagination(object):
    """
    Overlays an imagination onto an OPF model.
    
    """
    
    def __init__(model):
        self.model = model # opf.Model
        
    def imagine(self, func_list):
        """
        Imagines (predicts) the consequences of applying a given function to the model.
    
        The method accepts a set of functions, to permit a number of alternatives to be
        simultaneously assessed.  A given function is expected to mutate the model then use it
        to make a prediction.  The imagination class forks the model for each function invocation,
        providing a ephemeral/hypothetical model to the function.
    
        """
        
        # fork the model, then apply the sets of input sequences
        temp_path = tempfile.mkdtemp(prefix='nupic')
        self.model.save(temp_path)
        
        results = []
        for func in func_list:
            model_fork = CLAModel.load(temp_path)
            result = func(model_fork) # a list of predictions (one for each run)
            results.append(result)
        
        shutil.rmtree(temp_path)
        
        return results
        