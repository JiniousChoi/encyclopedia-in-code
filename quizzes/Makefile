test:
	@echo
	@echo ========== starting test ==========
	#find . -type f -name "*.py" -exec python3 {} \;
	find -type d -path ./00.organize.me -prune -o -type f -name "*.py" -exec python3 {} \;
	@echo ========== end of test ==========
	@echo

clean:
	@echo
	@echo ========== delete all pyc files ==========
	find . -type f -name "*.pyc" -delete
	find . -type d -name "__pycache__" -delete
	@echo ========== end of deletion ==========
	@echo
