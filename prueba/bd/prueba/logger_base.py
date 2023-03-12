import logging as log

log.basicConfig(
    level=log.DEBUG,
    format='%(asctime)s: %(levelname)s [%(filename)s]: %(lineno)s %(message)s  ',
    datefmt='%I:%M:%S:%p',
    handlers= [log.FileHandler('capa_datos.log'),log.StreamHandler()]
)

if name =='main':
    log.debug('Mensaje debug')
    log.warning('Mensaje de warning')
    log.error('Mensaje de error')
    log.critical('Mensaje de critical')