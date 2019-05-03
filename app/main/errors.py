from flask import render_template, request, jsonify, current_app
from . import main


@main.app_errorhandler(403)
def forbidden(e):
    if request.accept_mimetypes.accept_json and \
            not request.accept_mimetypes.accept_html:
        response = jsonify({'error': 'forbidden'})
        response.status_code = 403
        return response
    return render_template('403.html'), 403


@main.app_errorhandler(404)
def page_not_found(e):
    if request.accept_mimetypes.accept_json and \
            not request.accept_mimetypes.accept_html:
        response = jsonify({'error': 'not found'})
        response.status_code = 404
        return response
    return render_template('404.html'), 404


@main.app_errorhandler(500)
def internal_server_error(e):
    if request.accept_mimetypes.accept_json and \
            not request.accept_mimetypes.accept_html:
        response = jsonify({'error': 'internal server error'})
        response.status_code = 500
        return response
    return render_template('500.html'), 500

def ret_data(code=200, success=True, msg=''):
    return dict(code=code, success=success, msg=msg)

@main.app_errorhandler(Exception)
def internal_server_error(e):
    """
    global exception demo
    :param e:
    :return:
    """
    current_app.logger.debug('raise Exception debug')
    current_app.logger.info('raise Exception info')
    current_app.logger.warning('raise Exception warning')
    current_app.logger.error('raise Exception error')
    from app import db
    db.session.rollback()
    return jsonify(ret_data(code=500, success=False, msg=e.message))
