from gtda.time_series import SingleTakensEmbedding
from gtda.homology import VietorisRipsPersistence
from gtda.diagrams import BettiCurve
from gtda.plotting import plot_point_cloud
import gtda.plotting as gp
from datetime import datetime
from matplotlib import pyplot as plt


# The function takes in a 1D time series to transform into a higher dimensional point cloud
def make_point_cloud(heartbeat_):

    embedding_dimension_periodic = 3
    embedding_time_delay_periodic = 8
    embedder_periodic = SingleTakensEmbedding(
        parameters_type="fixed",
        n_jobs=2,
        time_delay=embedding_time_delay_periodic,
        dimension=embedding_dimension_periodic,
    )
    point_cloud_ = embedder_periodic.fit_transform(heartbeat_)

    return point_cloud_


def make_complex_w_pers_diag(point_cloud_):
    point_cloud_ = point_cloud_[None, :, :]

    homology_dimensions = [0, 1]

    periodic_persistence = VietorisRipsPersistence(
        homology_dimensions=homology_dimensions, n_jobs=-1
    )

    diag_ = periodic_persistence.fit_transform(point_cloud_)

    return diag_


def make_betti_curve(diag_):
    bc = BettiCurve(n_jobs=-1)
    betti_curve_ = bc.fit_transform(diag_)

    return betti_curve_