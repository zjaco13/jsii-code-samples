package hello

import (
	_jsii_ "github.com/aws/jsii-runtime-go/runtime"
	_init_ "github.com/zjaco13/jsii-code-samples/hello/jsii"
)

type HelloWorld interface {
	Opts() *ExtProps
	Fibonacci(num *float64) *float64
	SayHello(name *string) *string
}

// The jsii proxy struct for HelloWorld
type jsiiProxy_HelloWorld struct {
	_ byte // padding
}

func (j *jsiiProxy_HelloWorld) Opts() *ExtProps {
	var returns *ExtProps
	_jsii_.Get(
		j,
		"opts",
		&returns,
	)
	return returns
}


func NewHelloWorld(props *ExtProps) HelloWorld {
	_init_.Initialize()

	if err := validateNewHelloWorldParameters(props); err != nil {
		panic(err)
	}
	j := jsiiProxy_HelloWorld{}

	_jsii_.Create(
		"jsii-code-samples.HelloWorld",
		[]interface{}{props},
		&j,
	)

	return &j
}

func NewHelloWorld_Override(h HelloWorld, props *ExtProps) {
	_init_.Initialize()

	_jsii_.Create(
		"jsii-code-samples.HelloWorld",
		[]interface{}{props},
		h,
	)
}

func (h *jsiiProxy_HelloWorld) Fibonacci(num *float64) *float64 {
	if err := h.validateFibonacciParameters(num); err != nil {
		panic(err)
	}
	var returns *float64

	_jsii_.Invoke(
		h,
		"fibonacci",
		[]interface{}{num},
		&returns,
	)

	return returns
}

func (h *jsiiProxy_HelloWorld) SayHello(name *string) *string {
	if err := h.validateSayHelloParameters(name); err != nil {
		panic(err)
	}
	var returns *string

	_jsii_.Invoke(
		h,
		"sayHello",
		[]interface{}{name},
		&returns,
	)

	return returns
}

