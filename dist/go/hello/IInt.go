package hello

import (
	_jsii_ "github.com/aws/jsii-runtime-go/runtime"
)

type IInt interface {
	Foo() *string
	ImmutableNum() *float64
	MutableNum() *float64
	SetMutableNum(m *float64)
}

// The jsii proxy for IInt
type jsiiProxy_IInt struct {
	_ byte // padding
}

func (i *jsiiProxy_IInt) Foo() *string {
	var returns *string

	_jsii_.Invoke(
		i,
		"foo",
		nil, // no parameters
		&returns,
	)

	return returns
}

func (j *jsiiProxy_IInt) ImmutableNum() *float64 {
	var returns *float64
	_jsii_.Get(
		j,
		"immutableNum",
		&returns,
	)
	return returns
}

func (j *jsiiProxy_IInt) MutableNum() *float64 {
	var returns *float64
	_jsii_.Get(
		j,
		"mutableNum",
		&returns,
	)
	return returns
}

func (j *jsiiProxy_IInt)SetMutableNum(val *float64) {
	if err := j.validateSetMutableNumParameters(val); err != nil {
		panic(err)
	}
	_jsii_.Set(
		j,
		"mutableNum",
		val,
	)
}

