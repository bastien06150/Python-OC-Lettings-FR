from asyncio.log import logger

from django.shortcuts import render
import logging

logger = logging.getLogger(__name__)


def index(request):
    logger.info("Affichage de la page d'accueil.")
    return render(request, "index.html")


def triger_error(request):
    raise Exception("This is an error")
