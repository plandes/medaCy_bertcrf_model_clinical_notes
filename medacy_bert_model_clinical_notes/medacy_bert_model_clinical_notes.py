import os

from pkg_resources import resource_filename

from medacy.model.model import Model
from medacy.pipelines.bert_pipeline import BertPipeline
from medacy.pipeline_components.feature_extractors.text_extractor import TextExtractor
from medacy.pipeline_components.feature_overlayers.metamap.metamap_component import MetaMapOverlayer
from medacy.pipeline_components.learners.bert_learner import BertLearner
from medacy.pipeline_components.tokenizers.systematic_review_tokenizer import SystematicReviewTokenizer
from medacy.pipelines.base.base_pipeline import BasePipeline


PIPELINE_ARGS = {}


def load():
    entities = ['Drug', 'Form', 'Route', 'ADE', 'Reason', 'Frequency', 'Duration', 'Dosage', 'Strength']
    pipeline = BertPipeline(
        entities=entities, using_crf=True,
        pretrained_model='emilyalsentzer/Bio_ClinicalBERT',
        **PIPELINE_ARGS)
    model = Model(pipeline)
    model_directory = resource_filename('medacy_bert_model_clinical_notes', 'model')
    model_directory = os.path.join(model_directory, 'torch')
    model.load(model_directory)
    return model
