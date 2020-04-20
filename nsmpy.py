import time
import os
import random
import numpy as np

int_32 = 0
float_32 = 1
class MatrixErrors:
	def __init__(self): pass
	class MatrixShapeError(Exception):
		pass
	class GenerateMatrixDotError(Exception):
		pass
	class MatrixArgumentError(Exception):
		pass
	class ProductTypeNonExistError(Exception): 
		pass
	class ReshapeError(Exception):
		pass

class matrix:
	def __init__(self, array_data, shape, dtype=int_32):
		self.as_array = array_data
		self.type = dtype
		self.shape = shape
		if (self.shape[0] * self.shape[1] != len(self.as_array)):
			raise MatrixErrors.MatrixShapeError("Shape must match array_data length.")

	def __str__(self):
		str_arr = [str(x) for x in self.as_array]
		longest_arr = 0

		for x in str_arr: 
			if (len(x) > longest_arr): longest_arr = len(x)

		return_string = ""
		z = 0
		#first_run = True
		for x in str_arr:
			padding = longest_arr - len(x)
			return_string += (" " * padding)+" "
			return_string += x + " "
				
			if z % (self.shape[0]+1) == 0 and z != 0:
				return_string += "\n"
				first_run = False
			z += 1

		return return_string
	def __repr__(self):
		as_string = [str(x) for x in self.as_array]
		return "matrix(["+', '.join(as_string)+"])"
	def __len__(self): return len(self.as_array)
	def __getitem__(self, item): return self.as_array[item]
	def __setitem__(self, item, val): self.as_array[item] = val

	# these are the actual methods of the class
	def as_numpy_array(self):
		dtype = [np.int32, np.float32]
		dtype = dtype[self.type]
		x,y = [0,0]
		mat_b = []
		vec = []
		for i in range(0, len(self)):
			vec.append(self[y*self.shape[1] + x])
			x += 1
			if x == self.shape[0]:
				x = 0
				y += 1
				mat_b.append(vec)
				vec = []
		return np.array(mat_b, dtype)

	def add_element(self, element, new_shape):
		self.as_array.append(element)
		self.shape = new_shape
		if (self.shape[0] * self.shape[1] != len(self.as_array)):
			raise MatrixErrors.MatrixShapeError("Shape must match array_data length.")

	def get_type(self):
		return ["int_32", "float_32"][self.type]

	def matrix_mult(self, b_matrix, ptype="dot product", a_matrix=None):
		if (a_matrix == None): a_matrix = self
		try:
			if (b_matrix.shape[1] == a_matrix.shape[0]) and (a_matrix.shape[1] == b_matrix.shape[0]):
				x,y = [0,0]
				mat_a = []
				mat_b = []

				vec = []
				for i in range(0, len(b_matrix)):
					vec.append(b_matrix[y*b_matrix.shape[1] + x])
					x += 1
					if x == b_matrix.shape[0]:
						x = 0
						y += 1
						mat_b.append(vec)
						vec = []
				vec = []
				x,y = [0,0]
				for i in range(0, len(a_matrix)):
					vec.append(a_matrix[y*a_matrix.shape[1] + x])
					x += 1
					if x == a_matrix.shape[0]:
						x = 0
						y += 1
						mat_a.append(vec)
						vec = []
				if ptype == "dot product":
					A = np.array(mat_a)
					B = np.array(mat_b)

					C = np.dot(A, B)
					C_shape = C.shape
					C = C.flatten()
					C = C.tolist()
					return matrix(C, shape=C_shape)
				else:
					raise MatrixErrors.ProductTypeNonExistError("Type '"+str(ptype)+"' does not exist.")
			else:
				raise MatrixErrors.MatrixShapeError("b_matrix must have the opposite shape to the a_matrix.")
		except AttributeError:
			raise MatrixErrors.MatrixArgumentError("a_matrix or b_matrix must be of type 'matrix' or 'numpy.array().")
	def multiply(self, matrix_b, matrix_a=None):
		if matrix_a==None:matrix_a=self
		if (matrix_b.shape[0]*matrix_b.shape[1]) == (matrix_a.shape[0]*matrix_a.shape[1]):
			x1,x2,y1,y2 = [0,0,0,0]
			multiplied_matrix = []
			for i in range(0, matrix_a.shape[0]*matrix_a.shape[1]):
				multiplied_matrix.append((matrix_a[y1*matrix_a.shape[1]+x1]*matrix_b[y2*matrix_b.shape[1]+x2]))
				x1 += 1; x2+=1
				if x1 == matrix_a.shape[0]:
					x1 = 0
					y1+=1
				if x2 == matrix_b.shape[0]:
					x2 = 0
					y2+=1
			multiplied_matrix = matrix(multiplied_matrix, shape=matrix_a.shape)
			return multiplied_matrix
		else:
			raise MatrixErrors.MatrixShapeError("Multiplication of shapes A and B must be equal.")
	def flatten(self, matrix=None):
		if matrix ==None: matrix=self
		flattened_matrix = np.array(self.as_array).flatten()
		shape = flattened_matrix.shape
		flattened_matrix = flattened_matrix.tolist()
		return matrix(flattened_matrix, shape=shape)
	def reshape(self, new_shape):
		if (new_shape[0]*new_shape[1] == self.shape[0]*self.shape[1]): # the reshape is possible.
			self.shape = new_shape
		else:
			raise MatrixErrors.ReshapeError("Cannot reshape '"+str(self.shape)+"' to '"+str(new_shape)+"'.")
	def convert_to_list(self):
		x,y = [0,0]
		mat_b = []
		vec = []
		for i in range(0, len(self)):
			vec.append(self[y*self.shape[1] + x])
			x += 1
			if x == self.shape[0]:
				x = 0
				y += 1
				mat_b.append(vec)
				vec = []
		return mat_b
	def inverse(self):
		list_ = self.convert_to_list()
		arr = np.array(list_)
		inverse_ = np.linalg.inv(arr)

		inverse_ = inverse_.flatten().tolist()
		self.as_array = inverse_

	def generate_identity(self, r, c, start):
		mat = np.eye(r,c,k=start)
		sp = mat.shape
		mat = mat.flatten().tolist()
		return matrix(mat, shape=sp)

	def run_function_on_elements(self, function_callback):
		for x in range(0, len(self.as_array)):
			self.as_array[x] = function_callback(self.as_array[x])
if __name__ == "__main__":
	x = []
	for i in range(0, 1000):
		x.append(random.randint(0, 10000))

	test_matrix = matrix(x, shape=(4,250))

	print(test_matrix)
