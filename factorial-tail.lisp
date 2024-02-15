(defun factorial-tail (n &optional (acc 1))
	(if (zerop n)
		acc
		(factorial-tail(1- n)(* acc n))))
(print(factorial-tail 0 1))
(print(factorial-tail 1 1))
(print(factorial-tail 2 1))
(print(factorial-tail 5 1))
(print(factorial-tail 8 1))
(print(factorial-tail 10 1))
(print(factorial-tail 1000 1))

