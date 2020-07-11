# Note: this DB will be very inefficient. You will probably be much better off using other DBs.
# Another note: every element passed to the DB must be hashable
class Database:
	def __init__(self, columns, *args):
		self.columns = map(hash, columns)
		self.data = args
		self.hashed = [map(hash, x) for x in args]
			
	def query(self, querydict):
		pass
		
if __name__ == "__main__":
	d = Database(['id', 'thing'], [0, 'thing1'], [1, 'thing2'])
	print(d.query({
		'thing': 'thing1'
	})
