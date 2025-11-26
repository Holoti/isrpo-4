# Geometric Lib

Python library with math formulas for geometric figures.

## Features

### Circle
---

#### area(r)

```
Returns area of given circle.

Arguments:
	r (float): circle radius

Return value:
	area(r): circle area

Example:
	area(3) -> 28.274334
```

#### perimeter(r)

```
Return perimeter of given circle.

Arguments:
	r (float): circle radius

Return value:
	perimeter(r): circle perimeter

Example:
	perimeter(3) -> 18.849556
```

### Square
---

#### area(a)

```
Returns area of given square.

Arguments:
	a (float): square side

Return value:
	area(a): square area

Example:
	area(3) -> 9
```

#### perimeter(a)

```
Returns perimeter of given square.

Arguments:
	a (float): square side

Return value:
	perimeter(a): square perimeter

Example:
	perimeter(3) -> 12
```

### Rectangle
---

#### area(h, w)

```
Returns area of given rectangle.

Arguments:
	h (float): rectangle height
	w (float): rectangle width

Return value:
	area(h, w): rectangle area

Example:
	area(3, 4) -> 12
```

#### perimeter(h, w)

```
Returns perimeter of given rectangle.

Arguments:
	h (float): rectangle height
	w (float): rectangle width

Return value:
	area(h, w): rectangle perimeter

Example:
	perimeter(h, w) -> 14
```

### Triangle
---

#### area(a, h)

```
Returns area of given triangle.

Arguments:
	a (float): triangle base
	h (float): triangle height to corresponding base

Return value:
	area(a, h): triangle area

Example:
	area(3, 4) -> 6
```

#### perimeter(a, b, c)

```
Returns perimeter of given triangle.

Arguments:
	a (float): triangle 1st side
	b (float): triangle 2nd side
	c (float): triangle 3rd side

Return value:
	perimeter(a, b, c): triangle perimeter

Example:
	perimeter(3, 4, 5) -> 12
```

## History (recent to old)

* 45a5743 (HEAD -> new_features_501803) fix: rectangle.py: perimeter()
* 0b7d7b7 feat: triangle.py
* 7297e0d feat: rectangle.py
* d078c8d (origin/main, origin/HEAD, main) L-03: Docs added
* 8ba9aeb L-03: Circle and square added
