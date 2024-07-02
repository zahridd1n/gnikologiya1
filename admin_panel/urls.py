from django.urls import path

from admin_panel.views.result import ResultCreate, ResultList, ResultDelete, ResultUpdate
from admin_panel.views.comment import CommentCreate, CommentList, CommentDelete, CommentUpdate
from admin_panel.views.homepage import home
from admin_panel.views.log_in import log_in, log_out

urlpatterns = [
    path('home-page/', home, ),
    # -------------Natija Result--------------------------------
    path('result-create/', ResultCreate.as_view()),
    path('result-list/', ResultList.as_view()),
    path('result-delete/<int:id>/', ResultDelete.as_view()),
    path('result-update/<int:id>/', ResultUpdate.as_view()),
    # -------------Sharh Comment--------------------------------
    path('comment-create/', CommentCreate.as_view()),
    path('comment-list/', CommentList.as_view()),
    path('comment-delete/<int:id>/', CommentDelete.as_view()),
    path('comment-update/<int:id>/', CommentUpdate.as_view()),
    # -------------Login logout--------------------------------
    path('log-in/', log_in),
    path('log-out/', log_out),
]
