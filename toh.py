#!/usr/bin/env python

""" python/ game- Tower of Hanoi: This is a simple game which replicates a playable version of Tower of Hanoi allowing you to visually make move 
of rings from Peg to another such that if you are able to move the complete tower of rings from one of the peg to any of the other in minimum 
number of steps you win the game.
"""

import os

# Background display for the Tower of Hanoi.
def disp():
	print '      Peg-1           Peg-2           Peg-3	 '
	print ' 	*		*		*	 '
	print ' 	*		*		* 	 '
	print ' 	*		*		*	 '
	print ' 	*		*		*	 '
	print ' 	*		*		*	 '
	print '  	*		*		*	 '
	print ' 	*		*		*  	 '
	print ' 	*		*		*	 '
	print ' 	*		*		*	 '	
	print '/||||||||||||||||||||||||||||||||||||||||||||||||\ '
	print '|||||||||||||||||| Tower of Hanoi ||||||||||||||||'
	print '\||||||||||||||||||||||||||||||||||||||||||||||||/ '

# Function for cursor positioning.
def pos(x,y):
	return '\x1b[' + str(y) + ';' + str(x) + 'H'

# Function for notifying the steps of involved to solve Tower of Hanoi.
def toh(n,x,y,z):
	if n>0:
		toh(n-1,x,z,y)
		print '(Move from Peg-%g to Peg-%g)' % (x,y)
		toh(n-1,z,y,x)

a=[1,1,1,1,1,1,1,18]; # List of disks contained in Peg-1.
b=[1,1,1,1,1,1,1,18]; # List of disks contained in Peg-2.
c=[1,1,1,1,1,1,1,18]; # List of disks contained in Peg-3.
	 
#Function creates the rings to play with
def create(n):
	os.system('clear')
	disp()
	for i in range(n):
		for j in range(a[i]):
			if a[i]!=1:
				print pos(9-a[i]/2+j,10-i) + '#'
	for i in range(n):
		for j in range(b[i]):
			if b[i]!=1:
				print pos(25-b[i]/2+j,10-i) + '#'
	for i in range(n):
		for j in range(c[i]):
			if c[i]!=1:
				print pos(41-c[i]/2+j,10-i) + '#'
	print pos(0,20) + ' '

# Function to change the ring position.
def move(r):
	count=0
	print pos(0,20) + ' '
	fro=raw_input('From Peg: ')
	
	try:
		f=int(fro)		
	except:
		f=4
	
	# When moving from Peg-1.
	if f==1:
		# Loop to determine the index of the topmost ring in the peg.
		for i in range(r+1):
			print i,a[i]
			if a[i]!=1:
				continue
			else:
				break
		temp=a[i-1]
		a[i-1]=1
		create(r)
		to=raw_input('To Peg: ')
		
		try:
			t=int(to)		
		except:
			t=4
			
		if t==2:
			count+=1	
			for j in range(r+1):
				if b[j]!=1:
					continue
				else:
					break
			if b[j-1]>temp and b[j]==1:
				b[j]=temp
				
			else:
				a[i-1]=temp
				print pos(0,20) + 'Invalid Move!!!   (Press any key to continue)'	
				l=raw_input()
		
		elif t==3:
			count+=1
			for j in range(r+1):
				if c[j]!=1:
					continue
				else:
					break
			if c[j-1]>temp and c[j]==1:		
				c[j]=temp
			else:
				a[i-1]=temp
				print pos(0,20) + 'Invalid Move!!!   (Press any key to continue)'	
				l=raw_input()
				
		elif t==1:
			a[i-1]=temp
			create(r)
			
		elif t is not (1,2,3):
			a[i-1]=temp
			print pos(0,20) + 'Invalid Move!!!   (Press any key to continue)'
			l=raw_input()

	# When moving from Peg-2.
	elif f==2:
		# Loop to determine the topmost ring in the peg.
		for i in range(r+1):
			if b[i]!=1:
				continue
			else:
				break
		temp=b[i-1]
		b[i-1]=1
		create(r)
		to=raw_input('To Peg: ')
		
		try:
			t=int(to)		
		except:
			t=4		
		
		if t==1:
			count+=1
			for j in range(r+1):
				if a[j]!=1:
					continue
				else:
					break
			if a[j-1]>temp and a[j]==1:
				a[j]=temp
				
			else:
				b[i-1]=temp
				print pos(0,20) + 'Invalid Move!!!   (Press any key to continue)'	
				l=raw_input()
		
		elif t==3:
			count+=1
			for j in range(r+1):
				if c[j]!=1:
					continue
				else:
					break
			if c[j-1]>temp and c[j]==1:		
				c[j]=temp
			else:
				b[i-1]=temp
				print pos(0,20) + 'Invalid Move!!!   (Press any key to continue)'	
				l=raw_input()
				
		elif t==2:
			b[i-1]=temp
			create(r)
			
		elif t is not (1,2,3):
			b[i-1]=temp
			print pos(0,20) + 'Invalid Move!!!   (Press any key to continue)'
			l=raw_input()
	
	#When Moving from Peg-3.
	elif f==3:
		# Loop to determine the topmost ring in the peg.
		for i in range(r+1):
			if c[i]!=1:
				continue
			else:
				break
		temp=c[i-1]
		c[i-1]=1
		create(r)
		to=raw_input('To Peg: ')
		
		try:
			t=int(to)		
		except:
			t=4
		
		if t==1:
			count+=1
			for j in range(r+1):
				if a[j]!=1:
					continue
				else:
					break
			if a[j-1]>temp and a[j]==1:
				a[j]=temp
				
			else:
				a[i-1]=temp
				print pos(0,20) + 'Invalid Move!!!   (Press any key to continue)'	
				l=raw_input()
		
		elif t==2:
			count=+1
			for j in range(r+1):
				if b[j]!=1:
					continue
				else:
					break	
			if b[j-1]>temp and b[j]==1:		
				b[j]=temp
			else:
				c[i-1]=temp
				print pos(0,20) + 'Invalid Move!!!   (Press any key to continue)'	
				l=raw_input()
				
		elif t==3:
			c[i-1]=temp
			create(r)
			
		elif t is not (1,2,3):
			c[i-1]=temp
			print pos(0,20) + 'Invalid Move!!!   (Press any key to continue)'
			l=raw_input()
	elif f is not (1,2,3):
		print pos(0,20) + 'Invalid Move!!!  (Press any key to continue)'
		l=raw_input()

	return count		


def main():
	cout=0
	rings=raw_input('Enter the number of rings in tower of hanoi (max. 7 rings):')
	r=int(rings)
	k=r-1	# ring index starts with 0
	
	for i in range(r):	# creates a complete ring
		for j in range(i+1):
			a[k-i]=2*(j+1)+1
			
	os.system('clear')
	disp()
	create(r)
	d=a
	itr=2**r-1 # No. of iteration required to solve tower of hanoi.
	turns=range(itr+10)

	for turn in turns:
		cout+=move(r)
		create(r)

		if cout<=itr:
			
			if d==b or d==c:
				print 'You Won\n'
				break
		else:
			if d==b or d==c:
				print 'You lost but completed the Tower of Hanoi'
				print 'Better luck next time!!!\n'
				break
				
			print 'You exceeded valid number of steps'
			l=raw_input('Do you wish to continue!!!')
			if l=='y':
				create(r)
				continue
			else:
				print 'You lose\n'
				break	
				
	print 'Details:-\n'
	print '1. Step required to complete tower of hanoi with %g rings : %g' % (r,itr)
	print '2. Step taken by user to complete : ',cout
	print '\n'
	get=raw_input('Do you wish to know the generalised steps involved (y/n)')
	if get=='y':
		toh(r,1,2,3)
		print 'Thanx for Playing'
	else:
		print 'Thanx for Playing'
	 

if __name__=='__main__':
	main()
