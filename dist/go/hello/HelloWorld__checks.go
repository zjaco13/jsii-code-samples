//go:build !no_runtime_type_checking

package hello

import (
	"fmt"

	_jsii_ "github.com/aws/jsii-runtime-go/runtime"
)

func (h *jsiiProxy_HelloWorld) validateFibonacciParameters(num *float64) error {
	if num == nil {
		return fmt.Errorf("parameter num is required, but nil was provided")
	}

	return nil
}

func (h *jsiiProxy_HelloWorld) validateSayHelloParameters(name *string) error {
	if name == nil {
		return fmt.Errorf("parameter name is required, but nil was provided")
	}

	return nil
}

func validateNewHelloWorldParameters(props *ExtProps) error {
	if err := _jsii_.ValidateStruct(props, func() string { return "parameter props" }); err != nil {
		return err
	}

	return nil
}

