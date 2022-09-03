from utils.load import load_data
from models.multivariate_gaussian import mvg_models, mvg_evaluation

if __name__ == "__main__":

    # Load Data
    Train_Data, Train_Labels = load_data('Train')

    # Define Applications
    applications = [0.5, 0.1, 0.9]
    K = 5

    # Test Logistic Regression
    imbalanced = False
    lambda_list = [10**-5, 10**-4, 10**-3,
                   10**-2, 10**-1, 1, 10, 100, 1000, 10000]
    prior = 0.5
    options = {
        "m_pca": None,
        "gaussianize": False
    }

    mvg_models(Train_Data, Train_Labels, applications, K, options)

    # Evaluation
    Evaluation_Data, Evaluation_Labels = load_data('Test')
    mvg_evaluation(Train_Data, Train_Labels, Evaluation_Data,
                   Evaluation_Labels, "Tied", applications)