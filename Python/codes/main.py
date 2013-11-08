import inherit

philip = inherit.SchoolMember('Philip', 30)
jack = inherit.Teacher('Jack', 41, 30000)
cloud = inherit.Student('Cloud', 15, 94)

members = [jack,cloud]
for member in members:
	member.tell()
