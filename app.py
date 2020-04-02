from starter import create_app
if __name__ == '__main__':
    app = create_app()
    app.logger.info('init app')
    app.run(host=app.config.get('HOST', '0.0.0.0'),
            port=app.config.get('PORT', 5000))

