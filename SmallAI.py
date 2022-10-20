import sys
sys.path.append("clipit")
import clipit

# To reset settings to default
clipit.reset_settings()

# You can use "|" to separate multiple prompts
prompts = "underwater city"

# You can trade off speed for quality: draft, normal, better, best
quality = "normal"

# Aspect ratio: widescreen, square
aspect = "widescreen"

# Add settings
clipit.add_settings(prompts=prompts, quality=quality, aspect=aspect)

# Apply these settings and run
settings = clipit.apply_settings()
clipit.do_init(settings)
cliptit.do_run(settings)