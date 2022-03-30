
class Move():
	def u(cube):
		a=cube
		w,y,b,g,r,o=a['w'],a['y'],a['b'],a['g'],a['r'],a['o']
		# swap face-corner
		b[2][0],b[2][2],b[0][0],b[0][2]=b[2][2],b[2][0],b[0][2],b[0][0]
		b[0][0],b[2][2]=b[2][2],b[0][0]
		#  swap face-edge
		b[0][1],b[1][2],b[2][1],b[1][0]=b[1][2],b[0][1],b[1][0],b[2][1]
		b[0][1],b[2][1]=b[2][1],b[0][1]
		# swap corners
		w[0][2],o[0][2],r[0][2],y[0][2],w[0][0],o[0][0],r[0][0],y[0][0],w[0][1],o[0][1],r[0][1],y[0][1]=o[0][2],w[0][2],y[0][2],r[0][2],o[0][0],w[0][0],y[0][0],r[0][0],o[0][1],w[0][1],y[0][1],r[0][1]
		# o[0][2],w[0][2],y[0][2],r[0][2],o[0][0],w[0][0],y[0][0],r[0][0],o[0][1],w[0][1],y[0][1],r[0][1]
		w[0][2],y[0][2],w[0][0],y[0][0],w[0][1],y[0][1]=y[0][2],w[0][2],y[0][0],w[0][0],y[0][1],w[0][1]
		return a
	def uP(cube):
		a=cube
		w,y,b,g,r,o=a['w'],a['y'],a['b'],a['g'],a['r'],a['o']
		# swap face-corner
		b[2][0],b[2][2],b[0][0],b[0][2]=b[2][2],b[2][0],b[0][2],b[0][0]
		b[2][0],b[0][2]=b[0][2],b[2][0]
		#  swap face-edge
		b[0][1],b[1][2],b[2][1],b[1][0]=b[1][2],b[0][1],b[1][0],b[2][1]
		b[1][0],b[1][2]=b[1][2],b[1][0]	
		# swap corners
		w[0][2],o[0][2],r[0][2],y[0][2],w[0][0],o[0][0],r[0][0],y[0][0],w[0][1],o[0][1],r[0][1],y[0][1]=o[0][2],w[0][2],y[0][2],r[0][2],o[0][0],w[0][0],y[0][0],r[0][0],o[0][1],w[0][1],y[0][1],r[0][1]
		# o[0][2],w[0][2],r[0][2],r[0][2],o[0][0],w[0][0],r[0][0],r[0][0],o[0][1],w[0][1],r[0][1],r[0][1]
		o[0][2],r[0][2],o[0][0],r[0][0],o[0][1],r[0][1]=r[0][2],o[0][2],r[0][0],o[0][0],r[0][1],o[0][1]
		return a
	def d(cube):
		a=cube
		w,y,b,g,r,o=a['w'],a['y'],a['b'],a['g'],a['r'],a['o']
		# swap face-corner
		g[2][0],g[2][2],g[0][0],g[0][2]=g[2][2],g[2][0],g[0][2],g[0][0]
		g[0][0],g[2][2]=g[2][2],g[0][0]
		#  swap face-edge
		g[0][1],g[1][2],g[2][1],g[1][0]=g[1][2],g[0][1],g[1][0],g[2][1]
		g[0][1],g[2][1]=g[2][1],g[0][1]
		# swap corners
		w[2][0],r[2][0],o[2][0],y[2][0],w[2][2],r[2][2],o[2][2],y[2][2],w[2][1],r[2][1],o[2][1],y[2][1]=r[2][0],w[2][0],y[2][0],o[2][0],r[2][2],w[2][2],y[2][2],o[2][2],r[2][1],w[2][1],y[2][1],o[2][1]
		# o[0][2],w[0][2],y[0][2],o[0][2],o[0][0],w[0][0],y[0][0],o[0][0],o[0][1],w[0][1],y[0][1],o[0][1]
		w[2][0],y[2][0],w[2][1],y[2][1],w[2][2],y[2][2]=y[2][0],w[2][0],y[2][1],w[2][1],y[2][2],w[2][2]
		return a
	def dP(cube):
		a=cube
		w,y,b,g,r,o=a['w'],a['y'],a['b'],a['g'],a['r'],a['o']
		# swap face-corner
		g[2][0],g[2][2],g[0][0],g[0][2]=g[2][2],g[2][0],g[0][2],g[0][0]
		g[0][2],g[2][0]=g[2][0],g[0][2]
		#  swap face-edge
		g[0][1],g[1][2],g[2][1],g[1][0]=g[1][2],g[0][1],g[1][0],g[2][1]
		g[1][0],g[1][2]=g[1][2],g[1][0]
		# swap corners
		w[2][0],r[2][0],o[2][0],y[2][0],w[2][2],r[2][2],o[2][2],y[2][2],w[2][1],r[2][1],o[2][1],y[2][1]=r[2][0],w[2][0],y[2][0],o[2][0],r[2][2],w[2][2],y[2][2],o[2][2],r[2][1],w[2][1],y[2][1],o[2][1]
		# o[0][2],w[0][2],y[0][2],o[0][2],o[0][0],w[0][0],y[0][0],o[0][0],o[0][1],w[0][1],y[0][1],o[0][1]
		r[2][0],o[2][0],r[2][1],o[2][1],r[2][2],o[2][2]=o[2][0],r[2][0],o[2][1],r[2][1],o[2][2],r[2][2]
		return a
	def l(cube):
		a=cube
		w,y,b,g,r,o=a['w'],a['y'],a['b'],a['g'],a['r'],a['o']
		# swap face-corner
		o[2][0],o[2][2],o[0][0],o[0][2]=o[2][2],o[2][0],o[0][2],o[0][0]
		o[0][0],o[2][2]=o[2][2],o[0][0]
		#  swap face-edge
		o[0][1],o[1][2],o[2][1],o[1][0]=o[1][2],o[0][1],o[1][0],o[2][1]
		o[0][1],o[2][1]=o[2][1],o[0][1]
		# swap corners
		w[0][0],g[0][0],y[2][2],b[0][0],w[2][0],g[2][0],y[0][2],b[2][0],w[1][0],g[1][0],b[1][0],y[1][2]=g[0][0],w[0][0],b[0][0],y[2][2],g[2][0],w[2][0],b[2][0],y[0][2],g[1][0],w[1][0],y[1][2],b[1][0]
		# o[0][2],w[0][2],y[0][2],r[0][2],o[0][0],w[0][0],y[0][0],r[0][0],o[0][1],w[0][1],y[0][1],r[0][1]
		w[0][0],y[2][2],w[2][0],y[0][2],w[1][0],y[1][2]=y[2][2],w[0][0],y[0][2],w[2][0],y[1][2],w[1][0]
		return a
	def lP(cube):
		a=cube
		w,y,b,g,r,o=a['w'],a['y'],a['b'],a['g'],a['r'],a['o']
		# swap face-corner
		o[2][0],o[2][2],o[0][0],o[0][2]=o[2][2],o[2][0],o[0][2],o[0][0]
		o[2][0],o[0][2]=o[0][2],o[2][0]
		#  swap face-edge
		o[0][1],o[1][2],o[2][1],o[1][0]=o[1][2],o[0][1],o[1][0],o[2][1]
		o[1][2],o[1][0]=o[1][0],o[1][2]
		# swap corners
		w[0][0],g[0][0],y[2][2],b[0][0],w[2][0],g[2][0],y[0][2],b[2][0],w[1][0],g[1][0],b[1][0],y[1][2]=g[0][0],w[0][0],b[0][0],y[2][2],g[2][0],w[2][0],b[2][0],y[0][2],g[1][0],w[1][0],y[1][2],b[1][0]
		# o[0][2],w[0][2],y[0][2],r[0][2],o[0][0],w[0][0],y[0][0],r[0][0],o[0][1],w[0][1],y[0][1],r[0][1]
		g[0][0],b[0][0],g[2][0],b[2][0],g[1][0],b[1][0]=b[0][0],g[0][0],b[2][0],g[2][0],b[1][0],g[1][0]
		return a
	def r(cube):
		a=cube
		w,y,b,g,r,o=a['w'],a['y'],a['b'],a['g'],a['r'],a['o']
		# swap face-corner
		r[2][0],r[2][2],r[0][0],r[0][2]=r[2][2],r[2][0],r[0][2],r[0][0]
		r[0][0],r[2][2]=r[2][2],r[0][0]
		#  swap face-edge
		r[0][1],r[1][2],r[2][1],r[1][0]=r[1][2],r[0][1],r[1][0],r[2][1]
		r[0][1],r[2][1]=r[2][1],r[0][1]
		# swap corners
		w[2][2],b[2][2],y[0][0],g[2][2],w[0][2],b[0][2],y[2][0],g[0][2],w[1][2],b[1][2],g[1][2],y[1][0]=b[2][2],w[2][2],g[2][2],y[0][0],b[0][2],w[0][2],g[0][2],y[2][0],b[1][2],w[1][2],y[1][0],g[1][2]
		# o[0][2],w[0][2],y[0][2],r[0][2],o[0][0],w[0][0],y[0][0],r[0][0],o[0][1],w[0][1],y[0][1],r[0][1]
		w[2][2],y[0][0],y[2][0],w[0][2],w[1][2],y[1][0]=y[0][0],w[2][2],w[0][2],y[2][0],y[1][0],w[1][2]
		return a
	def rP(cube):
		a=cube
		w,y,b,g,r,o=a['w'],a['y'],a['b'],a['g'],a['r'],a['o']
		# swap face-corner
		r[0][0],r[2][0],r[0][2],r[2][2]=r[2][0],r[0][0],r[2][2],r[0][2]
		r[2][2],r[0][0]=r[0][0],r[2][2]
		#  swap face-edge
		r[0][1],r[1][2],r[2][1],r[1][0]=r[1][2],r[0][1],r[1][0],r[2][1]
		r[1][0],r[1][2]=r[1][2],r[1][0]
		# swap corners
		w[2][2],b[2][2],y[0][0],g[2][2],w[0][2],b[0][2],y[2][0],g[0][2],w[1][2],b[1][2],g[1][2],y[1][0]=b[2][2],w[2][2],g[2][2],y[0][0],b[0][2],w[0][2],g[0][2],y[2][0],b[1][2],w[1][2],y[1][0],g[1][2]
		b[2][2],g[2][2],b[0][2],g[0][2],b[1][2],g[1][2]=g[2][2],b[2][2],g[0][2],b[0][2],g[1][2],b[1][2]
		return a
	def f(cube):
		a=cube
		w,y,b,g,r,o=a['w'],a['y'],a['b'],a['g'],a['r'],a['o']
		# swap face-corner
		w[2][0],w[2][2],w[0][0],w[0][2]=w[2][2],w[2][0],w[0][2],w[0][0]
		w[0][0],w[2][2]=w[2][2],w[0][0]
		# swap face-edge
		w[0][1],w[1][2],w[2][1],w[1][0]=w[1][2],w[0][1],w[1][0],w[2][1]
		w[0][1],w[2][1]=w[2][1],w[0][1]
		# swap corners
		g[0][2],o[2][2],b[2][0],r[0][0],g[0][0],o[0][2],b[2][2],r[2][0],g[0][1],o[1][2],b[2][1],r[1][0]=o[2][2],g[0][2],r[0][0],b[2][0],o[0][2],g[0][0],r[2][0],b[2][2],o[1][2],g[0][1],r[1][0],b[2][1]

		b[2][0],g[0][2],b[2][2],g[0][0],b[2][1],g[0][1]=g[0][2],b[2][0],g[0][0],b[2][2],g[0][1],b[2][1]
		return a
	def fP(cube):
		a=cube
		w,y,b,g,r,o=a['w'],a['y'],a['b'],a['g'],a['r'],a['o']
		# swap face-corner
		w[2][0],w[2][2],w[0][0],w[0][2]=w[2][2],w[2][0],w[0][2],w[0][0]
		w[2][0],w[0][2]=w[0][2],w[2][0]
		# swap face-edge
		w[0][1],w[1][2],w[2][1],w[1][0]=w[1][2],w[0][1],w[1][0],w[2][1]
		w[1][0],w[1][2]=w[1][2],w[1][0]
		# swap corners
		# z=[[0][2],[2][2],[2][0],2[0][0]]
		g[0][2],o[2][2],b[2][0],r[0][0],g[0][1],o[1][2],b[2][1],r[1][0],g[0][0],o[0][2],b[2][2],r[2][0]=o[2][2],g[0][2],r[0][0],b[2][0],o[1][2],g[0][1],r[1][0],b[2][1],o[0][2],g[0][0],r[2][0],b[2][2]
		o[2][2],r[0][0],o[1][2],r[1][0],o[0][2],r[2][0]=r[0][0],o[2][2],r[1][0],o[1][2],r[2][0],o[0][2]
		return a
	def b(cube):
		a=cube
		w,y,b,g,r,o=a['w'],a['y'],a['b'],a['g'],a['r'],a['o']
		# swap face-corner
		y[2][0],y[2][2],y[0][0],y[0][2]=y[2][2],y[2][0],y[0][2],y[0][0]
		y[0][0],y[2][2]=y[2][2],y[0][0]
		# swap face-edge
		y[2][1],y[1][0],y[0][1],y[1][2]=y[1][0],y[2][1],y[1][2],y[0][1]
		y[0][1],y[2][1]=y[2][1],y[0][1]
		# swap corners
		r[2][2],b[0][2],o[0][0],g[2][0],r[0][2],b[0][0],o[2][0],g[2][2],r[1][2],b[0][1],o[1][0],g[2][1]=b[0][2],r[2][2],g[2][0],o[0][0],b[0][0],r[0][2],g[2][2],o[2][0],b[0][1],r[1][2],g[2][1],o[1][0]
		r[2][2],o[0][0],r[0][2],o[2][0],r[1][2],o[1][0]=o[0][0],r[2][2],o[2][0],r[0][2],o[1][0],r[1][2]
		return a
	def bP(cube):
		a=cube
		w,y,b,g,r,o=a['w'],a['y'],a['b'],a['g'],a['r'],a['o']
		# swap face-corner
		y[2][0],y[2][2],y[0][0],y[0][2]=y[2][2],y[2][0],y[0][2],y[0][0]
		y[2][0],y[0][2]=y[0][2],y[2][0]
		# swap face-edge
		y[2][1],y[1][0],y[0][1],y[1][2]=y[1][0],y[2][1],y[1][2],y[0][1]
		y[1][0],y[1][2]=y[1][2],y[1][0]
		# swap corners
		r[2][2],b[0][2],o[0][0],g[2][0],r[0][2],b[0][0],o[2][0],g[2][2],r[1][2],b[0][1],o[1][0],g[2][1]=b[0][2],r[2][2],g[2][0],o[0][0],b[0][0],r[0][2],g[2][2],o[2][0],b[0][1],r[1][2],g[2][1],o[1][0]
		b[0][2],g[2][0],b[0][0],g[2][2],b[0][1],g[2][1]=g[2][0],b[0][2],g[2][2],b[0][0],g[2][1],b[0][1]
		return a
class specMove():
	def u2(cub):
		[Move.u(cub) for i in range(2)]
		return cub
	def b2(cub):
		[Move.b(cub) for i in range(2)]
		return cub
	def f2(cub):
		[Move.f(cub) for i in range(2)]
		return cub
	def l2(cub):
		[Move.l(cub) for i in range(2)]
		return cub
	def r2(cub):
		[Move.r(cub) for i in range(2)]
		return cub
	def d2(cub):
		[Move.d(cub) for i in range(2)]
		return cub
	





# def m(arg):
# 	a=Cube('wwwwwwww bbbbbbbb gggggggg oooooooo rrrrrrrr yyyyyyyy')
# 	b=arg
# 	for i in range(len(arg)):
# 		a=Cube(toString(mov(b[i],a.cube)))
# 	a.show()


# def col(arg):
# 	# print(arg)
# 	a=Cube(arg)
# 	a.show()
# 	print()
# 	a=Cube(toString(mov('fP',a.cube)))
# 	a.show()


# def main(arg):
# 	b=arg.split(' ')
# 	if b[0]=='-m':m(' '.join(b[1:])
# 	elif b[0]=='-c':col(' '.join(b[1:]))
# 	else: print('duh')

# for i in b:
# 		a=Cube(toString(mov(i,a.cube)))
# 	a.show()