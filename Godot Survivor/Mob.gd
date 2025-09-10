extends CharacterBody2D

@onready var player = get_node("/root/Game/Player")
var health = 4
const SMOKE_SCENE = preload("res://smoke_explosion/smoke_explosion.tscn")

func _ready():
	%Slime.play_walk()

func _physics_process(delta):
	
	var direction = global_position.direction_to(player.global_position)
	velocity = direction * 200

	move_and_slide()
	
func take_damage(damage):
	health -= damage
	%Slime.play_hurt()
	
	if health <= 0:	
		queue_free()
		var smoke = SMOKE_SCENE.instantiate()
		add_sibling(smoke)
		smoke.global_position = global_position
