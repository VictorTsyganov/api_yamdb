from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(
    #добавить регулярное выражение
    basename='reviews'
)
router.register(
    #добавить регулярное выражение
    basename='comments'
)