(defun factorial (n)
	(if (zerop n)
		1
		(* n (factorial (1- n)))))
(print (factorial 0))
(print (factorial 1))
(print (factorial 2))
(print (factorial 5))
(print (factorial 8))
(print (factorial 10))
(print (factorial 1000))

