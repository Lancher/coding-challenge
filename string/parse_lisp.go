package string

import "fmt"
import "strconv"

func evaluate(expression string) int {
	namespace := make(map[string]int)
	return eval(expression, namespace)
}


func eval(exp string, namespace map[string]int) int {
	// exp is integer
	if exp[0] == '-' || 0 <= int(exp[0]) - int('0') && int(exp[0]) - int('0') <= 9 {
		i, _ := strconv.Atoi(exp)
		return i
	} else if exp[0] != '(' {
		return namespace[exp]
	}

	// remove head '(' tail ')'
	start := 0
	new_exp := exp[1:len(exp)-1]
	op := parse(new_exp, &start)

	// new namespace
	new_namespace := make(map[string]int)
	for k, v := range(namespace) {
		new_namespace[k] = v
	}

	// let
	if op == "let" {
		for start < len(new_exp) {
			key := parse(new_exp, &start)
			if len(new_exp) <= start {
				return eval(key, new_namespace)
			}
			val := parse(new_exp, &start)
			new_namespace[key] = eval(val, new_namespace)
		}
	// mult
	} else if op == "mult" {
		return eval(parse(new_exp, &start), new_namespace) * eval(parse(new_exp, &start), new_namespace)
	// add
	} else {
		return eval(parse(new_exp, &start), new_namespace) + eval(parse(new_exp, &start), new_namespace)
	}
	return 0
}


func parse(exp string, i *int) string {
	res := ""

	// pivot
	cnt := 0

	// parse first () or let_key or let_val
	for *i < len(exp) {
		if exp[*i] == ' ' {
			if res == "" {
				*i += 1
				continue
			}
			if cnt == 0 {
				*i += 1
				break
			} else {
				res += string(exp[*i])
				*i += 1
			}
		} else if exp[*i] == '(' {
			if cnt == 0 {
				if res == "" {
					res += string(exp[*i])
					*i += 1
					cnt += 1
				} else {
					break
				}
			} else {
				res += string(exp[*i])
				*i += 1
				cnt += 1
			}
		} else if exp[*i] == ')' {
			res += string(exp[*i])
			cnt -= 1
			if cnt == 0 {
				*i += 1
				break
			}
			*i += 1
		} else {
			res += string(exp[*i])
			*i += 1
		}
	}
	return res
}

