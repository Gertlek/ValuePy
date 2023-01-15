import pickle

class function:
    def load_pickle(filepath):
        """Load a Stock object from a pickle file"""
        with open(filepath, 'rb') as f:
            return pickle.load(f)
