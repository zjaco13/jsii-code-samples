//go:build no_runtime_type_checking

package hello

// Building without runtime type checking enabled, so all the below just return nil

func (h *jsiiProxy_HelloWorld) validateFibonacciParameters(num *float64) error {
	return nil
}

func (h *jsiiProxy_HelloWorld) validateSayHelloParameters(name *string) error {
	return nil
}

func validateNewHelloWorldParameters(props *ExtProps) error {
	return nil
}

