package hello


type ExtProps struct {
	Name *string `field:"required" json:"name" yaml:"name"`
	GoodName *bool `field:"optional" json:"goodName" yaml:"goodName"`
}

