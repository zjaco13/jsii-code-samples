//go:build no_runtime_type_checking

package hello

// Building without runtime type checking enabled, so all the below just return nil

func (j *jsiiProxy_IInt) validateSetMutableNumParameters(val *float64) error {
	return nil
}

