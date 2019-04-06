from arrai import Arrai
import arrai as ar
if __name__ == "__main__":
	a = Arrai([[100000000,2,3,4,5],[3,4,7,1,2],[2,1,3,3,4],[3,4,7,1,2],[1,2,3,4,5]])
	b = Arrai([[6], [5], [4],[3],[2]])
	print("A: \n%s\n" % a)
	print("B: \n%s\n" % b)
	c = a.mul(b)
	print("A * B: \n%s\n" % c)
	print("A': \n%s\n" % a.transpose())
	d = a.mul(a.transpose())
	print("AA': \n%s\n" % d)

	e = Arrai(3)
	print(10+a)
	print("A: \n%s\n" % a)
	print(a  * e)
	print(e * a)
	print(a)
	print(a-5)
	print(a*3)
	print(a.col(0))
	print("A(1,:): \n%s\n" % a.row(1))
	print(ar.zum(a))
	print(ar.zum(a,2))
	print("sum row of A: \n%s\n" % ar.zum(a))
	print("dot(A,A,1): \n%s\n" % ar.dot(a,a,1))
	print("dot(A,A,2): \n%s\n" % ar.dot(a,a,2))
	print(ar.dot(Arrai([1,2,3]), Arrai([2,3,5])))
	print(ar.dot(Arrai([1,2,3]), Arrai([[2],[3],[5]])))
	print(ar.dot(Arrai([[2],[3],[5]]), Arrai([1,2,3])))
	print("A: \n%s\n" % a)
	print("A: \n%s\n" % (a.col(0) - a.col(1)))
	print("A: \n%s\n" % a.swap_row(0, 1))
	print("A: \n%s\n" % a.swap_col(2, 3))
	print("A: \n%s\n" % a)

	f = Arrai([[1,2,-1],[2,3,-1],[-2,0,22],[3,17,23]])
	g = Arrai([[1,2,3],[2,4,5],[4,7,9]])
	print("RREF: %s" % ar.to_RREF(f))
	print("RREF: %s" % ar.to_RREF(g))
	print("Inverse: %s" % ar.inverse(g))
	print("F/G: %s" % (f/g))
	h = Arrai([[5,1,8],[4,-2,0],[6,7,4]])
	print("Rank H: %s" % ar.rank(h))
	print("RREF H: %s" % ar.to_RREF(h))
	print("Inverse H: %s" % ar.inverse(h))
	i = Arrai([[46],[12],[50]])
	import arrai.helpers
	print("solution H|I: %s" % arrai.helpers.helper_RREF(h, i)["B"])
	h = Arrai([[36.9,38.1,39.2,17.7,46.0,12.2,30.6,6.0,33.3,2.5,29.0,30.9,35.4,5.9,13.0,42.3,7.2,9.1,42.8,12.8,10.8,1.5,31.4,14.6,8.6,45.5,2.6,48.9,22.9,31.5,34.3,13.4,13.5,49.1,31.8,20.0,0.0,8.0,11.7,19.5,20.3,3.5,18.4,10.1,13.6,47.3,17.2,19.2,17.3,15.3,],[32.5,28.8,4.6,35.0,41.5,28.4,43.7,38.1,38.1,22.1,26.6,41.2,39.2,39.0,27.2,17.6,37.9,18.1,17.4,22.8,19.6,31.3,32.1,39.8,34.1,30.3,43.1,19.9,11.2,23.5,34.3,38.5,8.8,19.0,6.2,19.3,19.1,33.9,39.4,35.7,5.0,25.7,10.7,4.9,26.8,21.5,31.4,20.8,23.9,40.4,],[46.8,41.5,19.8,26.1,7.9,3.8,24.9,32.9,8.8,10.9,0.8,32.5,49.7,48.3,35.8,42.9,5.2,7.7,39.2,5.5,9.0,24.5,45.8,27.0,12.5,45.7,48.6,5.2,14.8,20.9,38.5,46.0,42.3,48.6,31.9,11.1,9.4,21.7,33.6,48.2,4.8,40.1,31.5,8.9,44.1,34.8,12.5,42.8,44.3,49.8,],[6.6,29.7,18.5,39.0,30.3,6.3,26.8,3.6,13.3,39.9,6.5,22.5,9.8,42.8,41.7,31.1,9.3,6.5,37.4,41.4,4.2,14.9,5.3,16.3,8.3,4.3,30.4,39.1,39.2,38.4,18.8,21.0,20.8,13.4,29.1,32.0,4.6,1.3,32.8,3.6,45.2,18.2,46.4,8.1,43.2,6.4,8.0,2.5,29.6,16.6,],[46.4,19.7,5.4,16.3,45.0,47.6,32.4,36.3,18.9,46.8,23.9,5.1,28.2,43.6,26.6,35.9,26.4,28.0,44.9,12.9,48.6,4.3,4.5,49.0,8.9,21.8,7.3,18.1,39.3,40.2,23.9,36.3,22.1,14.3,42.1,19.4,7.6,16.3,37.5,6.5,28.2,18.7,18.2,29.5,40.0,1.2,12.6,38.7,8.1,42.4,],[13.8,25.4,16.8,24.8,17.5,6.6,14.6,12.9,11.7,10.0,20.7,30.5,39.6,15.8,1.1,30.0,39.8,47.5,42.8,43.1,0.5,34.2,9.2,42.5,20.7,13.6,16.1,44.5,44.9,18.6,15.4,37.2,24.3,37.9,43.1,20.5,42.3,24.4,22.8,7.9,19.2,12.0,41.4,31.3,39.9,26.8,21.0,7.3,28.8,4.2,],[36.1,34.7,32.7,27.9,44.2,4.9,35.2,28.2,8.1,8.5,13.7,10.6,26.5,34.6,4.7,36.7,35.6,17.6,47.1,40.6,17.3,29.2,13.3,37.0,49.8,43.1,0.5,31.6,10.0,26.4,17.9,5.5,3.7,41.2,41.3,20.6,41.7,16.3,22.8,14.9,1.6,33.1,48.2,20.6,25.4,48.4,42.1,7.9,37.1,3.8,],[21.1,37.0,13.0,29.5,30.5,4.5,42.2,45.6,38.3,39.3,21.3,41.9,29.8,29.2,43.3,17.8,33.7,46.4,0.8,27.3,46.8,19.6,31.5,2.2,1.7,37.8,31.7,16.7,14.4,16.6,49.0,18.8,25.4,18.9,31.2,23.9,3.1,47.0,28.4,4.1,38.0,32.8,18.9,44.4,34.4,18.4,43.1,32.9,18.1,41.1,],[49.8,28.4,31.3,35.3,0.0,45.7,1.6,40.0,29.4,34.0,49.3,4.1,4.1,45.3,6.8,10.4,22.7,21.4,25.2,17.1,9.6,10.9,20.2,29.8,24.9,36.6,16.2,16.8,25.1,27.5,12.4,30.8,24.0,24.7,4.1,37.4,10.1,49.6,38.8,7.7,12.2,42.7,1.7,30.2,26.5,44.0,10.8,4.3,49.0,44.3,],[47.4,43.9,12.7,8.7,13.3,36.3,18.6,49.6,48.5,14.9,27.7,1.1,14.3,23.6,15.6,15.8,3.4,20.7,42.8,37.8,18.2,6.8,49.2,44.8,36.3,22.0,44.3,49.3,42.6,3.4,32.2,33.5,29.3,19.9,35.4,0.6,15.2,11.3,34.1,19.9,13.3,31.3,0.9,49.0,23.0,39.1,47.1,34.4,47.4,19.1,],[48.4,13.5,22.7,19.0,13.8,23.0,48.1,49.2,45.6,30.4,24.4,5.5,24.0,9.0,4.4,47.0,8.3,18.4,44.8,7.8,37.5,7.9,21.7,40.7,48.0,6.2,16.8,15.0,23.0,31.0,1.5,48.1,28.1,30.8,22.8,3.7,33.7,43.8,8.1,38.6,32.8,2.0,23.6,25.3,26.4,38.7,16.2,20.3,44.4,36.7,],[45.8,20.4,12.8,13.2,45.1,48.0,20.9,42.3,17.1,40.3,6.5,15.9,13.4,8.9,49.0,44.9,12.4,34.3,43.4,8.4,24.7,11.5,29.1,12.3,36.0,34.6,21.7,22.6,29.6,18.9,21.2,18.8,37.3,18.1,26.7,2.5,30.0,39.4,41.5,15.8,45.4,10.3,5.7,39.1,9.7,40.8,42.5,23.2,27.9,8.1,],[19.6,26.9,17.9,24.4,10.2,43.1,33.7,38.2,1.9,47.8,31.7,40.6,36.3,25.3,13.3,14.2,37.6,4.9,14.7,45.4,16.7,2.1,49.7,28.2,48.5,48.8,33.3,10.0,9.9,36.5,23.2,47.2,17.1,41.1,4.7,19.9,1.6,7.9,1.9,14.2,20.5,38.0,27.0,18.2,16.0,4.3,18.0,17.6,18.4,10.9,],[39.8,14.2,32.6,5.6,34.9,45.3,6.3,26.9,32.1,44.5,30.8,24.5,44.4,1.5,14.2,28.8,10.4,49.5,39.4,30.8,13.6,7.0,13.8,4.4,12.3,9.7,20.8,40.2,33.4,7.2,49.9,9.1,47.3,17.3,38.6,48.8,38.1,23.2,46.1,3.5,25.5,18.6,25.3,21.3,23.1,18.5,36.2,49.4,20.2,13.3,],[25.5,21.6,20.3,24.6,35.8,25.9,17.5,28.2,41.6,15.7,13.3,24.8,25.6,26.8,49.6,4.9,18.3,48.6,44.6,39.2,29.5,2.7,10.5,21.3,26.6,30.2,11.9,28.2,12.8,8.8,43.8,18.8,16.9,30.8,17.3,39.9,24.2,15.1,43.8,46.6,0.9,13.3,31.9,25.7,30.1,34.9,27.0,44.3,46.0,40.6,],[15.1,26.7,45.8,10.9,35.7,5.0,47.1,5.3,21.0,19.4,8.4,35.7,27.5,21.7,15.2,21.8,30.1,17.7,40.0,8.4,7.2,38.8,3.9,14.7,47.6,32.7,11.9,0.1,27.8,26.1,39.8,30.2,28.6,23.7,43.2,4.4,42.9,20.7,46.5,4.7,26.3,36.1,12.2,14.5,44.9,13.4,22.0,18.4,45.1,2.3,],[10.5,35.2,8.7,4.2,20.6,1.1,5.6,3.3,23.3,16.8,20.9,46.2,17.9,15.6,4.4,13.9,46.3,19.1,31.9,1.3,26.6,7.2,33.5,2.3,21.9,23.1,11.9,37.6,43.5,39.7,42.9,12.7,16.8,29.3,42.2,40.9,48.4,27.2,12.5,49.5,7.2,8.7,2.2,16.1,46.6,2.7,5.1,35.3,49.6,39.5,],[20.6,38.7,18.7,28.8,38.3,26.3,1.8,42.8,24.6,29.3,44.5,34.1,46.7,17.5,13.9,38.0,44.5,4.8,15.0,43.6,42.4,12.7,40.9,35.0,44.1,44.1,35.2,10.0,35.4,22.1,44.1,24.5,11.4,17.9,5.6,34.9,36.5,49.2,10.4,44.3,29.9,28.4,36.6,36.0,25.5,49.4,13.5,9.1,32.3,37.0,],[26.8,24.5,33.4,21.9,15.4,20.0,38.1,27.9,49.2,29.8,8.6,26.2,15.9,45.4,11.7,11.8,44.7,10.2,25.6,19.7,36.8,24.6,33.3,46.7,19.2,27.4,11.0,7.1,9.7,46.0,41.4,12.1,28.2,8.0,30.9,16.1,20.5,35.5,49.5,22.7,13.7,40.1,45.6,33.2,18.0,39.7,18.7,20.6,7.5,18.9,],[44.4,38.1,1.9,26.5,42.1,33.4,13.7,36.7,42.9,10.8,26.8,9.7,19.3,47.9,23.6,18.3,37.6,0.6,8.2,37.5,40.2,27.5,36.1,14.9,18.6,48.4,18.1,37.7,17.3,29.8,2.6,45.3,23.7,17.3,20.8,24.0,15.5,47.2,45.2,37.8,45.3,17.1,33.6,33.8,16.9,30.9,7.2,34.8,43.0,16.4,],[21.1,44.5,25.8,15.6,15.9,25.7,41.4,26.7,22.3,27.5,48.1,38.3,11.4,29.4,34.0,29.1,33.9,14.5,21.8,36.4,39.3,16.3,29.8,29.4,2.1,3.6,46.8,16.7,49.5,31.7,22.3,15.3,47.6,40.9,7.8,6.5,42.0,22.9,8.6,42.2,42.3,14.7,6.7,38.3,11.9,49.3,12.6,32.4,48.6,1.9,],[32.0,14.3,8.6,42.9,35.4,24.4,36.2,34.9,12.9,36.6,23.6,32.4,32.8,21.3,23.9,1.2,44.5,35.1,7.8,49.4,17.9,8.2,25.8,15.1,35.7,2.1,22.9,43.5,24.9,44.9,33.3,9.9,40.3,8.6,39.2,6.4,0.7,14.4,6.2,4.3,15.1,19.6,33.6,3.7,20.9,6.5,25.5,35.8,45.4,22.0,],[24.6,2.3,37.9,7.9,45.4,21.2,2.3,22.0,17.3,49.4,44.5,18.4,19.6,16.5,38.9,47.3,10.3,11.8,46.3,47.7,18.2,25.2,30.9,11.1,1.2,14.3,8.6,12.7,1.6,2.5,46.2,21.7,20.3,30.1,23.8,38.1,43.1,0.2,42.1,12.1,11.2,18.5,30.0,22.7,48.6,31.6,20.2,17.9,49.3,10.3,],[41.0,17.1,33.1,35.7,33.6,6.3,24.1,9.8,31.6,16.2,29.9,11.4,23.5,46.0,19.4,45.6,18.0,28.7,2.9,44.8,20.1,0.5,9.2,0.8,8.9,39.1,43.5,34.4,8.9,12.7,3.0,46.3,1.8,15.2,5.5,5.2,29.8,43.5,1.2,24.5,14.7,27.2,2.9,2.5,0.6,34.5,49.5,34.9,50.0,34.5,],[46.6,25.2,25.2,25.9,29.2,35.1,29.5,10.2,38.6,25.2,31.8,32.9,0.9,27.4,38.4,40.9,19.7,48.2,8.1,25.2,24.7,37.7,45.5,16.3,16.9,10.8,38.7,30.4,46.2,21.7,22.2,21.9,39.8,24.2,37.8,48.5,13.3,44.1,28.6,27.8,32.0,20.5,39.7,14.6,7.1,39.1,22.8,26.0,21.9,13.9,],[38.5,31.9,15.2,45.1,36.8,32.9,2.1,30.6,42.0,24.6,28.4,17.5,8.1,19.7,26.4,3.7,37.9,44.6,29.3,24.0,8.3,8.9,46.8,27.2,32.1,8.8,3.7,16.7,19.2,27.1,0.7,18.0,40.8,1.2,30.2,1.4,5.1,45.8,20.1,21.6,13.2,5.0,6.8,15.4,47.5,7.1,40.7,28.9,4.8,36.1,],[40.7,6.3,36.5,26.3,18.0,37.3,28.8,11.8,1.6,31.2,23.6,43.3,27.0,7.8,8.9,15.9,48.4,0.5,36.3,18.4,25.9,3.7,10.1,21.8,21.6,29.3,21.6,30.6,22.8,11.7,22.8,36.9,39.0,19.5,37.3,46.9,22.4,49.2,10.9,7.4,5.1,37.6,18.1,40.9,37.3,32.0,41.4,37.9,38.3,38.5,],[12.9,11.7,21.1,16.7,17.2,47.2,42.2,12.9,48.2,29.8,47.5,42.8,4.6,23.3,37.5,46.2,14.1,18.6,26.8,15.8,38.1,32.6,33.1,31.4,17.6,0.6,4.7,0.5,43.0,31.8,30.3,3.2,45.5,49.3,32.0,26.1,10.7,42.8,40.1,46.1,46.3,18.1,42.8,24.6,10.5,20.3,48.3,14.0,2.5,4.5,],[22.0,11.4,22.7,36.8,13.0,1.4,18.9,10.4,47.4,1.6,49.7,10.0,40.8,25.6,43.9,42.8,40.9,22.4,22.1,15.7,17.0,2.4,20.8,20.4,42.4,0.6,33.0,5.0,1.1,2.2,31.8,48.9,45.4,11.6,37.1,23.5,49.3,26.2,6.6,45.9,24.6,0.4,27.7,10.9,43.3,38.9,20.2,11.6,42.1,46.5,],[17.1,30.7,38.3,16.9,42.9,4.8,37.0,17.2,3.2,12.9,4.7,30.9,27.8,42.5,18.2,5.6,43.4,10.2,9.8,46.3,13.3,40.0,32.2,12.2,2.4,5.1,17.1,45.9,33.4,36.7,19.6,32.7,7.9,12.5,27.2,37.6,6.6,32.3,8.1,38.2,49.7,8.4,24.4,16.9,26.0,11.4,14.6,17.8,3.3,13.9,],[26.6,28.1,15.6,30.7,0.8,35.9,42.1,27.3,17.3,32.9,23.7,33.9,21.0,0.6,37.7,44.9,40.1,7.9,3.0,45.6,18.1,32.8,21.7,13.0,33.4,44.0,17.6,19.9,37.1,19.8,33.1,15.5,24.1,5.7,40.9,35.1,19.5,19.5,4.4,25.9,6.5,17.1,45.7,38.6,42.7,29.0,3.0,42.9,19.2,44.0,],[23.7,5.9,40.1,40.9,30.2,22.6,41.4,50.0,19.4,44.1,41.1,3.0,3.4,20.7,29.0,37.9,12.5,32.4,38.1,1.8,41.2,34.8,26.9,20.6,5.5,6.4,30.4,8.8,40.8,3.5,41.7,22.1,44.8,17.1,32.6,32.7,24.5,25.5,40.6,41.4,11.8,22.0,40.7,1.0,15.8,8.2,4.8,34.2,17.9,25.1,],[45.2,4.1,11.6,20.7,23.7,47.1,49.7,47.7,34.6,30.8,25.9,36.0,15.3,3.9,43.7,32.9,40.3,45.3,3.8,33.2,49.9,26.2,13.6,10.1,11.3,18.4,30.5,4.6,17.0,7.9,27.5,4.7,35.5,18.5,12.7,3.8,23.4,25.1,15.9,21.7,35.7,30.8,25.0,41.1,1.6,36.9,32.1,34.1,25.3,23.1,],[24.8,19.4,32.9,12.5,17.4,11.7,38.0,6.5,43.4,46.9,11.7,22.8,46.8,3.5,37.2,22.1,4.9,5.2,32.0,18.5,43.8,34.4,7.4,12.7,37.9,23.3,19.3,44.3,7.2,29.8,10.8,35.8,27.9,19.0,12.7,29.6,38.1,45.7,29.4,25.5,42.4,15.9,9.1,48.7,46.8,28.0,17.1,33.4,26.1,34.3,],[28.3,8.5,10.1,49.9,11.8,35.2,36.5,16.8,26.7,39.7,32.2,47.7,13.2,23.5,10.0,41.9,37.0,11.8,7.9,27.4,34.5,44.9,0.1,0.4,8.4,26.2,48.7,44.4,2.1,0.3,18.5,1.5,35.3,42.0,32.8,0.9,25.2,14.5,9.0,21.8,10.0,29.3,23.9,16.5,30.3,13.0,45.5,21.2,23.5,34.9,],[28.5,7.4,29.0,31.9,30.4,9.4,41.5,35.7,23.4,42.3,28.9,37.5,13.6,24.0,21.1,28.4,36.6,9.4,16.6,9.5,26.2,47.1,11.3,4.0,42.0,29.5,34.1,33.9,24.7,48.6,18.0,10.2,41.5,34.2,45.0,13.5,10.5,41.1,10.1,21.2,19.7,46.4,47.5,28.7,42.7,12.8,36.5,19.7,44.9,47.4,],[10.4,2.7,32.4,37.4,12.4,11.5,5.4,20.8,8.2,35.6,26.6,7.9,9.0,11.9,46.2,41.7,24.1,36.8,41.1,8.0,28.4,13.9,41.1,24.7,17.9,26.6,4.9,33.4,10.6,44.9,15.6,18.4,23.1,46.5,9.5,19.8,17.5,40.1,7.8,44.6,40.7,17.4,17.5,33.6,12.1,18.4,8.9,11.1,32.4,48.4,],[49.1,6.1,44.1,22.2,6.2,9.1,3.5,28.7,9.5,24.3,1.9,45.2,47.7,46.5,17.3,48.8,10.1,28.9,38.8,17.5,27.8,46.9,44.9,29.9,6.1,22.6,27.2,24.8,35.9,27.2,48.0,30.0,21.6,2.9,45.6,36.8,38.7,21.6,29.0,40.4,31.9,3.4,16.5,23.8,24.5,24.9,23.5,39.1,41.0,7.3,],[23.9,41.5,17.7,15.8,22.2,21.6,29.6,8.2,31.1,43.4,17.9,15.4,12.4,46.7,40.1,44.4,17.7,30.2,38.6,14.6,28.9,38.4,1.8,17.7,37.2,27.6,29.5,16.1,37.3,44.4,21.1,12.7,43.6,22.8,0.7,25.8,35.9,28.2,22.5,16.3,0.1,16.4,43.8,31.2,40.0,10.1,25.3,21.1,7.3,0.2,],[16.6,32.2,13.6,16.1,3.6,34.5,16.8,35.0,10.2,8.3,25.5,23.6,23.4,18.9,20.0,5.4,47.4,27.1,25.8,10.9,46.8,43.6,4.9,46.7,47.5,41.5,42.6,16.4,17.8,44.2,19.7,10.6,4.9,31.6,47.3,26.3,12.4,49.5,1.0,3.4,33.6,16.4,17.6,21.0,28.9,14.9,33.9,10.4,3.3,6.7,],[18.4,31.8,34.6,23.1,3.7,41.3,42.8,15.5,9.1,33.2,37.0,45.2,25.0,25.2,32.4,28.6,22.0,8.2,3.5,19.2,27.0,44.4,1.3,33.1,30.8,49.5,6.6,44.2,43.5,15.3,17.6,30.1,13.0,5.5,29.1,47.2,14.9,7.6,19.3,38.9,6.7,2.1,31.5,29.0,5.0,36.2,44.4,29.0,21.5,13.2,],[37.9,28.9,31.1,4.9,39.8,25.2,49.0,25.3,39.3,9.9,3.4,31.8,37.2,4.1,0.2,45.3,47.7,7.5,25.6,48.0,5.5,44.4,1.9,27.4,37.7,41.3,48.4,10.6,1.9,19.9,44.6,45.4,32.6,41.4,5.6,29.6,34.1,25.5,22.8,38.2,2.0,13.1,39.3,47.5,9.8,15.2,27.4,15.9,43.8,10.5,],[19.3,35.8,6.7,20.2,42.5,35.2,46.8,41.1,32.4,35.1,24.1,37.1,2.8,38.7,35.0,10.7,3.3,29.1,10.5,35.5,40.5,29.4,10.9,35.5,18.8,28.7,40.0,48.3,48.8,36.5,45.6,9.6,15.5,37.9,41.2,10.3,6.9,31.4,28.0,36.5,4.6,37.5,18.9,39.2,26.1,49.1,26.2,49.4,12.8,4.9,],[41.7,23.0,39.3,18.2,32.6,19.0,31.6,48.5,20.3,44.9,27.7,47.4,40.5,46.1,46.1,34.0,23.3,27.8,11.7,23.6,7.2,21.3,9.0,24.1,41.3,39.3,38.5,11.1,17.5,17.4,30.1,4.0,24.5,27.9,41.1,8.2,45.3,10.5,28.4,31.1,0.3,30.7,6.2,11.0,49.9,24.4,26.6,3.0,0.2,6.8,],[24.9,27.6,34.8,2.3,15.0,6.0,12.6,36.4,33.3,18.7,22.8,8.5,23.3,18.4,6.0,35.4,42.1,8.8,21.4,40.3,39.3,30.7,42.3,49.9,3.5,44.1,26.1,3.1,45.3,30.4,30.3,13.0,6.3,10.1,8.6,31.6,38.8,9.5,4.4,28.4,18.7,36.7,37.6,28.3,23.6,40.3,8.4,1.4,21.1,29.2,],[0.3,30.5,5.8,15.6,8.1,34.6,2.6,31.2,36.2,26.1,39.3,12.0,14.7,28.1,8.1,38.6,45.9,11.3,1.9,33.8,34.1,14.2,41.5,41.4,27.1,2.6,29.2,12.1,35.2,1.7,33.0,10.1,40.5,36.3,18.3,48.3,33.2,12.0,34.5,40.2,14.3,48.2,7.0,22.1,42.0,26.2,49.1,11.2,26.5,5.9,],[38.3,46.3,25.5,33.7,1.7,17.6,20.9,28.2,17.5,21.0,25.9,18.8,15.7,1.1,10.6,47.7,8.0,29.4,5.5,41.0,15.3,49.8,28.8,3.3,50.0,9.3,25.0,7.5,24.6,43.0,15.2,46.4,12.7,19.5,28.7,11.3,3.8,15.1,44.9,37.1,18.2,0.6,24.4,29.3,37.6,32.0,36.3,13.5,32.7,49.1,],[31.1,13.0,24.1,39.4,13.8,35.7,22.6,46.0,18.7,25.7,19.2,17.1,8.7,16.4,16.4,21.2,2.9,13.0,42.6,0.5,19.6,34.9,5.8,43.1,10.2,36.0,8.5,17.7,27.8,6.4,48.2,44.5,33.8,18.3,44.7,33.9,39.6,19.0,41.8,38.7,9.7,37.9,20.5,7.5,5.6,11.8,2.6,5.5,13.1,34.6,],[29.3,43.8,42.0,29.7,47.3,45.2,5.8,17.8,31.2,2.9,8.2,19.5,46.0,6.3,0.6,12.9,7.3,20.8,21.0,28.2,46.1,44.4,30.8,46.8,48.2,46.5,46.8,7.5,7.9,42.5,49.6,24.1,19.6,23.2,1.0,39.3,18.2,42.4,40.1,41.0,15.7,3.3,16.2,46.9,11.7,11.5,21.5,35.7,25.0,14.2,],[49.9,33.5,36.1,33.9,35.5,39.9,13.8,23.2,43.3,29.0,6.7,15.2,23.1,46.4,8.6,3.6,35.3,46.4,4.1,29.8,22.1,17.1,38.9,32.3,14.7,21.4,10.6,3.4,6.5,14.6,2.7,42.8,0.9,28.8,27.2,22.4,24.1,5.2,17.1,23.4,11.8,31.2,48.1,21.8,26.1,17.1,42.7,3.8,2.4,15.0,],])
	i = Arrai([[47.8,],[3.1,],[44.7,],[2.5,],[37.6,],[22.2,],[21.1,],[41.4,],[21.5,],[46.1,],[21.5,],[12.0,],[19.3,],[1.9,],[28.5,],[49.2,],[42.3,],[30.3,],[18.8,],[45.9,],[13.5,],[46.2,],[18.9,],[35.2,],[11.4,],[48.5,],[5.7,],[12.8,],[16.8,],[7.1,],[36.4,],[23.7,],[12.0,],[30.6,],[22.7,],[1.2,],[42.1,],[30.7,],[19.8,],[33.3,],[1.6,],[19.9,],[8.5,],[17.9,],[8.6,],[7.5,],[10.2,],[26.6,],[14.2,],[42.1,],])
	print("solution H|I: %s" % arrai.helpers.helper_RREF(h, i)["B"])
	print("A: %s" % h)
	print("B: %s" % i)
	for p in range(1):
		j = arrai.helpers.helper_RREF(h, i)["B"]
	print("solution Ax|B: %s" % j)


