import numpy as np
import pandas as pd
import xgboost as xgb
import datetime
import sklearn.model_selection
import os
import json


class AuthorDoctorEntityResolver:
    """
    A reusable class that saves a classifier with associated metadata
    """
    
    def __init__(self, model_dir: str, model_type: str = 'xgb'):
        # ^what we pass between functions 
        self.model = (self._initialize_xgb_model() if model_type == 'xgb'
                      else self._initialize_random_forests())
        self.metadata = {}
        self.model_dir = model_dir

    
    def train(self, features: pd.DataFrame, labels: pd.Series):
        """Train our classifier with features to predict labels

        Args:
            features (pd.DataFrame): a dataframe of features --
            te components used for calculations which may be created 
            for the data
            labels (pd.Series): a set of associated labels per row --
            the goal of the classifier
        """
        # train-test-split?
        features, features_test, labels, labels_test = (
            sklearn.model_selection(features, labels, test_size=0.2))
        self.model.fit(features, labels)
        # save below becasue they are not reprodicible
        self.metadata['training_date'] = datetime.datetime.now().strftime('%Y%m%d')
        self.metadata['training_rows'] = len(labels)
        self.metadata['accuracy'] = self.assess(features_test, labels_test)

    
    def predict(self, features: pd.DataFrame, proba: bool = False) -> np.ndarray:
        """Use a trained model to predict the output

        Args: 


        Returns:
        """
        if len(self.metadata) == 0:
            raise ValueError('MOdel must be trained first.')
        
        if proba:
            return self.model.predict_proba(features)[:, 0]
        return self.model.predict(features)
    
    def assess(self, features: pd.DataFrame, labels: pd.Series) -> float:
        """COmpute the accuracy of our model

        Args:
            features (pd.DataFrame): input features
            labels (pd.Series): known labels

        Returns:
            float: the accuracy of the model
        """
        pred_labels = self.predict(features)
        return(pred_labels == labels).sum()/len(labels)
    
    
    def save(self, filename: str, overwrite: bool = False):
        """Save filename location model_path on hard drive"""
        if len(self.metadata) == 0:
            raise ValueError('Model must be trained before saving.')
        
        today = datetime.datetime.now().strftime('%y%m%d')
        if filename[:6] != today:
            filename = f'{today}_{filename}'

        if os.path.splitext(filename)[1] != '.json':
            filename = filename + '.json'
        
        path = os.path.join(self.model_dir, filename)
        metadata_path = os.path.splitext(path)[0] + '_metadata.json'
        
        # Pickle is dangerous in rare cases...
        # ...

        if not overwrite and (os.path.exists(path) or
                              os.path.exists(metadata_path)):
            raise FileExistsError('Cannot overwrite existing file')

        self.model.save_model(path)
        with open(meatdata_path) as fo:
            json.dump(self.metadata, fo)

    def load(self, filename: str):

        path = os.path.join(self.model_dir, filename)
        metadata_path = os.path.splitext(path)[0] + '_metadata.json'
        self.model.load_model(path)

        with open(meatdata_path) as fr:
            json.dump(self.metadata, fr)

        self.metadata

    # labels - output from classifier
    # features - info used to make prediction
    # 3 classes: binary, multi-class, regression

    