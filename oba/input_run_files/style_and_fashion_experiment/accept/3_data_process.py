from oba.data_processer import WEBSHRINKER_CREDENTIALS, DataProcesser

style_and_fashion_experiment_accept_data_processer = DataProcesser(
    "style_and_fashion_experiment_accept", WEBSHRINKER_CREDENTIALS
)

style_and_fashion_experiment_accept_data_processer.filter_ads(
    non_ads=True, unspecific_ads=True
)
style_and_fashion_experiment_accept_data_processer.update_crawling_data_process()
