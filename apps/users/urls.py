from django.urls import include, path
from django.conf.urls import url
from rest_framework.routers import DefaultRouter
from . import views

# router = DefaultRouter()
# router.register('marque', views.MarqueViewSet)
# router.register('web_user', views.UserProfileViewSet)
# router.register('modele', views.ModeleViewSet)
# router.register('version', views.VersionViewSet)
# router.register('couleur', views.CouleurViewSet)
# router.register('option', views.OptionViewSet)
# router.register('vehicule', views.VehiculeViewSet)
# router.register('stock_upload', views.StockUploadView, base_name='stock_upload')
# router.register('ligne_tarif', views.LigneTarifViewSet)
# router.register('ligne_tarif_upload', views.LigneTarifUploadView, base_name='ligne_tarif_upload')
# router.register('subscription', views.SubscriptionViewSet)
# router.register('modele_images', views.ModeleImageViewSet)
# router.register('modele_videos', views.ModeleVideoViewSet)
# router.register('category', views.CategoryViewSet)
# router.register('modele_favorite', views.ModeleFavoriteViewSet)
# router.register('version_favorite', views.VersionFavoriteViewSet)
# router.register('compose_vehicule', views.ComposeVehiculeView, base_name='compose_vehicule')
# router.register('commande', views.CommandeViewSet)
# router.register('annonce', views.AnnonceViewSet)
# router.register('offre', views.OffreViewSet)
# router.register('reserver_vehicule', views.ReserverVehiculeView, base_name='reserver_vehicule')
# router.register('set_password', views.SetPasswordView, base_name='set_password')


urlpatterns = [
    # path('', include(router.urls)),
    path('auth_social/', views.AuthSocial.as_view()),
]
