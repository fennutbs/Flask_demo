from flask import Blueprint
# 路由用analysis开头
analysis_bp = Blueprint('analysis', __name__, url_prefix='/analysis')



from . import views