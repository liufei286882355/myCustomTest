//
//  LFTextView.m
//  LFTextView
//
//  Created by 刘飞 on 2017/8/11.
//  Copyright © 2017年 刘飞. All rights reserved.
//

#import "LFTextView.h"

#define LFScreenWidth [UIScreen mainScreen].bounds.size.width
#define LFScreenHeight [UIScreen mainScreen].bounds.size.height


@implementation LFTextView
{
    UIView *containView;///<外围包裹的灰色的背景view
    
    UITextView *contentTextView;///<输入内容的textview
    
    UILabel *placeholderLabel;///<占位内容label
    
    CGFloat textHeight;///<保存的高度
    
}
-(instancetype)initWithFrame:(CGRect)frame {
    self = [super initWithFrame:frame];
    if (self) {
        [self createUI];
        textHeight = 0;
        [[NSNotificationCenter defaultCenter] addObserver:self selector:@selector(showCommentView:) name:UIKeyboardDidShowNotification object:nil];
        [[NSNotificationCenter defaultCenter] addObserver:self selector:@selector(hideCommentView:) name:UIKeyboardDidHideNotification object:nil];
        UITapGestureRecognizer *tap = [[UITapGestureRecognizer alloc]initWithTarget:self action:@selector(tapViewHideKeyboard:)];
        [self addGestureRecognizer:tap];
    }
    return self;
}
-(void)createUI {
    
}







@end
