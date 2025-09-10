extends CharacterBody2D

signal health_depleted
var health = 100.0
const DAMAGE_RATE = 2.0

func _ready():
	%PlayerHealth.max_value = health
	
func _physics_process(delta):
	var direction = Input.get_vector(
		"move_left",
		"move_right",
		"move_up",
		"move_down",)
	
	velocity = direction*600	
	
	if velocity:
		%HappyBoo.play_walk_animation()
	else:
		%HappyBoo.play_idle_animation()
	move_and_slide()
	
	var overlapping_mobs = %HurtBox.get_overlapping_bodies()
	health -= DAMAGE_RATE * overlapping_mobs.size() * delta
	%PlayerHealth.value = health
	if health <= 0.0:
		health_depleted.emit()
		get_tree().paused = true
		
		
	
