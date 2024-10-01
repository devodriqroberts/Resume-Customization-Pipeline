ARGS = $(filter-out $@,$(MAKECMDGOALS))

resume:
	@if [ "$(ARGS)" = "" ]; then \
		echo "Usage: make resume <company> <job_url>"; \
		exit 1; \
	fi
	docker run --rm -it --env-file .env -v "$(PWD):/app" resume-tailor:latest $(word 1, $(ARGS)) $(word 2, $(ARGS))

# Allows passing arguments to Makefile
# Usage : make resume <company> <job_url>
%:
	@: