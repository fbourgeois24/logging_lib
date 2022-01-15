def logger(name="", existing=None, level=logging.INFO, format='%(asctime)s:%(name)s:%(levelname)s:%(message)s', stream_handler = True, file_handler = True, filename = ""):
	""" configurer un logger et renvoyer l'objet configuré
		name = nom du nouveau logger à créer
		existing = logger existant à configurer
		level = niveau du logger (DEBUG, INFO, WARNING, ERROR ou CRITICAL)
		format = format des messages de log
		stream_handler = Vrai s'il faut l'activer
		file_handler = Vrai s'il faut l'activer
		filename = Nom du fichier de sortie (utilisé par exemple pour renvoyer la sortie des logger de différents modules vers le même fichier)
	"""

	if existing is not None:
		# Si un logger existant a été passé, on reprend son nom
		name = existing.name
	elif name == "":
		# Si pas de nom et pas de logger existant on lève une erreur
		raise TypeError("Au moins un nom (pour un nouveau logger) ou un logger existant doivent être passés en paramètre")
	
	if existing is None:
		# Si aucun logger existant n'a été passé, on en crée un nouveau
		log = logging.getLogger(name)
	else:
		# Si un logger existant a été passé on l'utilise
		log = existing
	# On définit le niveau de log
	log.setLevel(level)
	# Format des messages
	formatter = logging.Formatter(format)
	if filename == "" and name != "":
		# Si pas de nom de fichier fourni on utilise le nom
		filename = name + ".log"
	elif filename == "" and name == "":
		# Si pas de nom et pas de nom de fichier
		raise TypeError("Aucun nom ou nom de fichier fourni")
	elif len(filename.split(".")) < 2:
		# Si le nom de fichier n'a pas encore d'extension
		filename += ".log"
	if file_handler:	
		# Si un file_handler doit être ajouté
		file_handler = logging.FileHandler(filename)
		file_handler.setFormatter(formatter)
		log.addHandler(file_handler)
	if stream_handler:	
		# Si un stream_handler doit être ajouté
		stream_handler = logging.StreamHandler()
		stream_handler.setFormatter(formatter)
		log.addHandler(stream_handler)
	return log
