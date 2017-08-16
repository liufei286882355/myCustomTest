//
//  TestCollectionViewController.m
//  LFTextView
//
//  Created by 刘飞 on 2017/8/15.
//  Copyright © 2017年 刘飞. All rights reserved.
//

#import "TestCollectionViewController.h"

#define ScreenWidth [UIScreen mainScreen].bounds.size.width
#define ScreenHeight [UIScreen mainScreen].bounds.size.height

@interface TestCollectionViewController ()


@property (nonatomic, strong) UICollectionView *mainCollectionView;

@end

@implementation TestCollectionViewController

- (void)viewDidLoad {
    [super viewDidLoad];
    
    
    
}





-(UICollectionView *)mainCollectionView {
    if (!_mainCollectionView) {
        _mainCollectionView = [[UICollectionView alloc]initWithFrame:CGRectMake(0, 64, ScreenWidth, ScreenHeight - 64)];
        
    }
    return _mainCollectionView;
}




@end
